#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re
import sys

ARCHIVE_DIR = Path('archive/originals')
CORE_DIR = Path('bundles/core')
PRO_DIR = Path('bundles/pro-addon')

H1_RE = re.compile(r'^# (\d+)\) (.+)$')


def normalize_links(line: str) -> str:
    result = []
    i = 0
    while i < len(line):
        if line[i] == '[':
            end_text = line.find(']', i)
            if end_text != -1 and end_text + 1 < len(line) and line[end_text + 1] == '(':
                start_url = end_text + 2
                j = start_url
                depth = 1
                while j < len(line) and depth > 0:
                    if line[j] == '(':
                        depth += 1
                    elif line[j] == ')':
                        depth -= 1
                    j += 1
                if depth == 0:
                    text = line[i + 1:end_text]
                    result.append(f'[{text}](LINK)')
                    i = j
                    continue
                # Fallback: use first closing parenthesis if unbalanced
                fallback = line.find(')', start_url)
                if fallback != -1:
                    text = line[i + 1:end_text]
                    result.append(f'[{text}](LINK)')
                    i = fallback + 1
                    continue
        result.append(line[i])
        i += 1
    return ''.join(result)


def remove_duplicate_first_h1(lines: list[str]) -> list[str]:
    first_h1 = None
    out = []
    for line in lines:
        if first_h1 is None and line.startswith('# '):
            first_h1 = line
            out.append(line)
            continue
        if first_h1 and line == first_h1:
            continue
        out.append(line)
    return out


def remove_duplicate_h1_any(lines: list[str]) -> list[str]:
    seen = set()
    out = []
    for line in lines:
        if line.startswith('# '):
            if line in seen:
                continue
            seen.add(line)
        out.append(line)
    return out


def load_lines(path: Path) -> list[str]:
    return path.read_text(encoding='utf-8').splitlines()


def first_h1(lines: list[str]) -> str | None:
    for line in lines:
        if line.startswith('# '):
            return line
    return None


def compare_normal(original: Path, refactored: Path, errors: list[str]) -> None:
    orig_lines = remove_duplicate_first_h1(load_lines(original))
    ref_lines = remove_duplicate_first_h1(load_lines(refactored))

    orig_h1 = first_h1(orig_lines)
    ref_h1 = first_h1(ref_lines)

    if orig_h1 is None or ref_h1 is None:
        errors.append(f"Missing H1 in comparison: {original} or {refactored}")
        return

    ref_h1_index = ref_lines.index(ref_h1)
    ref_lines[ref_h1_index] = orig_h1

    orig_norm = [normalize_links(line) for line in orig_lines]
    ref_norm = [normalize_links(line) for line in ref_lines]

    if orig_norm != ref_norm:
        errors.append(f"Content mismatch: {original} -> {refactored}")


def compare_artifacts(original: Path, artifacts_dir: Path, errors: list[str]) -> None:
    orig_lines = load_lines(original)
    headings = []
    seen_nums = set()
    for line in orig_lines:
        match = H1_RE.match(line)
        if match:
            num = int(match.group(1))
            if num in seen_nums:
                continue
            seen_nums.add(num)
            headings.append((num, line))

    if len(headings) != 40:
        errors.append(f"Expected 40 artifact headings, found {len(headings)} in {original}")
        return

    combined_lines: list[str] = []
    for num, heading_line in headings:
        pattern = f"Artifact {num:02d} —"
        matches = [p for p in artifacts_dir.glob('*.md') if p.name.startswith(pattern)]
        if len(matches) != 1:
            errors.append(f"Expected single artifact file for {pattern}, found {len(matches)}")
            return
        artifact_lines = load_lines(matches[0])
        if not artifact_lines or not artifact_lines[0].startswith('# '):
            errors.append(f"Artifact missing H1: {matches[0]}")
            return
        artifact_lines[0] = heading_line
        combined_lines.extend(artifact_lines)

    orig_norm = remove_duplicate_h1_any([normalize_links(line) for line in orig_lines])
    combined_norm = remove_duplicate_h1_any([normalize_links(line) for line in combined_lines])

    if orig_norm != combined_norm:
        errors.append("Artifact split mismatch: combined artifacts do not match original mega-page")


def main() -> int:
    errors: list[str] = []

    bundle_files = {p.name: p for p in CORE_DIR.rglob('*.md')}
    bundle_files.update({p.name: p for p in PRO_DIR.rglob('*.md')})

    for original in ARCHIVE_DIR.glob('*.md'):
        if original.name.startswith('1) Vision & Success Criteria — How to Build the Ar'):
            artifacts_dir = CORE_DIR / 'Engineering OS — CORE/01 BUILD FLOW (THE SPINE)/Artifacts'
            compare_artifacts(original, artifacts_dir, errors)
            continue

        orig_lines = load_lines(original)
        orig_h1 = first_h1(orig_lines)
        if not orig_h1:
            errors.append(f"Missing H1 in original: {original}")
            continue
        expected_name = f"{orig_h1[2:].strip()}.md"
        ref_path = bundle_files.get(expected_name)
        if not ref_path:
            errors.append(f"Missing refactored file for {original.name} (expected {expected_name})")
            continue
        compare_normal(original, ref_path, errors)

    if errors:
        print('VERIFY: FAIL')
        for error in errors:
            print(f"- {error}")
        return 1

    print('VERIFY: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main())
