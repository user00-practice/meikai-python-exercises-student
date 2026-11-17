"""プログラム作成問題の自動チェック

使い方（プロジェクトのフォルダで実行）:
    python tools/check.py            # 自分のプログラム（exercises）をチェック
    python tools/check.py ch04       # 第4章だけチェック

各問題のプログラムに決められた入力を与えて実行し、
表示が期待どおりかどうかを確かめます。
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def run_test(folder: Path, file: str, stdin: str) -> str:
    """フォルダを一時フォルダにコピーし、そこでプログラムを実行して表示を返す"""
    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp) / folder.name
        shutil.copytree(folder, work, ignore=shutil.ignore_patterns('__pycache__'))
        result = subprocess.run(
            [sys.executable, file],
            input=stdin, capture_output=True, text=True, encoding='utf-8',
            cwd=work, timeout=10,
            env={**os.environ, 'PYTHONIOENCODING': 'utf-8', 'PYTHONUTF8': '1'},
        )
        if result.returncode != 0:
            return '［エラー］\n' + result.stderr.strip().splitlines()[-1] if result.stderr else '［エラー］'
        return result.stdout


def main() -> None:
    args = sys.argv[1:]
    # --answer：answer/ フォルダのプログラムをチェックする（answer/ がある場合のみ）
    target = 'answer' if '--answer' in args else 'exercises'
    if not (ROOT / target).is_dir():
        print(f'{target}/ フォルダが見つかりません。')
        sys.exit(1)
    chapters = [a for a in args if a.startswith('ch')]
    tests = json.loads((ROOT / 'tools' / 'tests.json').read_text(encoding='utf-8'))
    if chapters:
        tests = [t for t in tests if t['ch'] in chapters]

    ok = 0
    for t in tests:
        folder = ROOT / target / t['ch']
        label = f"{t['ch']}/{t['file']}"
        try:
            actual = run_test(folder, t['file'], t['stdin'])
        except subprocess.TimeoutExpired:
            actual = '［時間切れ：無限ループになっていませんか？］'
        if actual == t['expect']:
            ok += 1
            print(f'○ {label}')
        else:
            print(f'× {label}')
            print('   入力：', repr(t['stdin']))
            print('   期待：', repr(t['expect']))
            print('   実際：', repr(actual))
    print(f'\n{ok} / {len(tests)} 件 正解')


if __name__ == '__main__':
    main()
