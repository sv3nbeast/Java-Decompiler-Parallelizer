# Java-Decompiler-Parallelizer
Java Decompiler Parallelizer 是一个基于Python的多进程反编译工具，可以快速高效地处理大量的 .jar 和 .class 文件。该工具使用了 CFR 反编译器，并利用多进程技术充分利用当前机器的CPU资源，以加速反编译过程。

**以下介绍由AI生成：**

## 功能特性

- **自动适配CPU核心数**：根据当前机器的CPU核心数自动调整并发进程数，最大化利用系统资源。
- **支持多种文件格式**：可以反编译 `.jar` 和 `.class` 文件，并将反编译结果输出到指定目录。
- **高效处理**：通过多进程并行处理大量文件，提高反编译速度。
- **易于使用**：只需提供待反编译文件的目录路径即可开始反编译过程。

## 使用说明

1. **克隆项目**
```
git clone https://github.com/yourusername/JavaDecompilerParallelizer.git
cd JavaDecompilerParallelizer
```
2. **安装CFR反编译器**

下载 CFR反编译器 并将其放置在项目目录下。

3. **运行反编译脚本**
  ```
  python decompile_multiprocess.py /path/to/your/directory
  ```
  其中，`/path/to/your/directory` 是包含 `.jar` 和 `.class` 文件的目录路径。

## 项目结构
- `decompile_multiprocess.py`：主脚本文件，包含反编译功能的实现。
- CFR-0.152.jar：CFR反编译器（需自行下载）。
## 贡献指南
  欢迎任何形式的贡献！您可以通过提交Issue或Pull Request来帮助改进本项目。

## 许可证
  本项目采用MIT许可证，详细信息请参见LICENSE文件。
