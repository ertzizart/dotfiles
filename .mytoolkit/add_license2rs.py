import os
import concurrent.futures
import argparse

LICENSE_HEADER = """/*
    Copyright 2025 Name <name@anymail.com>

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
*/

"""

def process_rs_file(file_path):
    
    try:
        with open(file_path, 'r+', encoding='utf-8') as f:
            content = f.read()
            
            if content.startswith(LICENSE_HEADER):
                return f"Skipped (already has license): {file_path}"
            
            if content.startswith('#!'):
                end_of_first_line = content.find('\n') + 1
                if end_of_first_line == 0:
                    end_of_first_line = len(content)
                
                new_content = (
                    content[:end_of_first_line] + 
                    '\n' + 
                    LICENSE_HEADER + 
                    content[end_of_first_line:]
                )
            else:
                new_content = LICENSE_HEADER + content
            
            f.seek(0)
            f.write(new_content)
            f.truncate()
            
        return f"Added license to: {file_path}"
    
    except Exception as e:
        return f"Error processing {file_path}: {str(e)}"

def find_rs_files(root_dir):
    rs_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.rs'):
                rs_files.append(os.path.join(dirpath, filename))
    return rs_files

def main():
    parser = argparse.ArgumentParser(description='Add license header to Rust files')
    parser.add_argument('--workers', type=int, default=os.cpu_count(),
                        help='Number of parallel workers (default: CPU count)')
    args = parser.parse_args()

    root_dir = os.getcwd()
    rs_files = find_rs_files(root_dir)
    
    if not rs_files:
        print("No .rs files found in current directory and subdirectories.")
        return
    
    print(f"Found {len(rs_files)} .rs files. Processing with {args.workers} workers...")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        results = list(executor.map(process_rs_file, rs_files))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()