import os
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed

# 指定要反编译的目录
directory = sys.argv[1]

def decompile(file_path, output_dir):
    command = f'java -jar CFR-0.152.jar {file_path} --outputdir {output_dir}'
    print(command)
    os.system(command)

def process_file(root, file):
    file_path = os.path.join(root, file)
    if file.endswith('.jar'):
        output_dir = os.path.join(os.getcwd(), 'outfiles', file.replace('.jar', ''))
    elif file.endswith('.class'):
        output_dir = os.path.join(os.getcwd(), 'outfiles', file.replace('.class', ''))
    else:
        return
    decompile(file_path, output_dir)

def main():
    # 获取当前机器的 CPU 核心数
    max_workers = os.cpu_count()
    print(f'Using {max_workers} workers for processing')

    # 使用 ProcessPoolExecutor 进行多进程处理
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.jar') or file.endswith('.class'):
                    futures.append(executor.submit(process_file, root, file))

        # 等待所有进程完成
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    main()
