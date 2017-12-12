# nvim-cmake-proj

## Aboud

* nvim cmake plugin

## Requirements

* nvim 
* python3
* cmake

## Instalation for dein.vim

```
[[plugins]]
repo = 'honeytrap15/nvim-cmake-proj'
```

## Quick start

open cmake project root.

```zsh
% tree example_project
example_project
├── CMakeLists.txt
├── include
│   └── main.hpp
└── src
└── main.cpp
% nvim example_project
```

Execute 'CMakeReload' command. It generates vim-cmake-build directory.

```
:CMakeReload
```

Execute 'CMakeBuild' command. It generates vim-cmake-build directory and run build.

```
:CMakeBuild
```

This plugin output build log in new panel.

```
```
