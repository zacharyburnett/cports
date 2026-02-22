pkgname = "vicinae"
pkgver = "0.19.9"
pkgrel = 1
build_style = "cmake"
configure_args = [
    "-DCMAKE_POLICY_VERSION_MINIMUM=3.5",
    "-DBUILD_TESTS=OFF",  # Build test suites for various vicinae components
    "-DIGNORE_CCACHE=OFF",  # Always ignore ccache even if it is installed
    "-DLTO=ON",  # Enable Link Time Optimization (LTO). This will result in better performance, but greatly increased compile time. (Gentoo chads can't live without this)
    "-DNOSTRIP=OFF",  # Never strip debug symbols from the binary, even in release mode. Note that symbols are never stripped for debug releases.
    "-DINSTALL_NODE_MODULES=ON",  # Install required node_modules dependencies as part of the build process. You can turn this off if you have another way to install the node_modules, but they are still required build the project."
    "-DWAYLAND_LAYER_SHELL=ON",  # Enable support for the layer shell Wayland protocol
    "-DTYPESCRIPT_EXTENSIONS=ON",  # Enable support for extensions built with React/Typescript (no browser involved)
    "-DPREFER_STATIC_LIBS=OFF",  # When available, link to a library statically instead of dynamically
    "-DFETCHCONTENT_FULLY_DISCONNECTED=OFF",
    "-DUSE_SYSTEM_PROTOBUF=ON",  # Use system protobuf instead of building it from source
    "-DUSE_SYSTEM_ABSEIL=ON",  # Use system abseil (libabsl) instead of building it from source
    "-DUSE_SYSTEM_CMARK_GFM=OFF",  # Use system cmark-gfm (github's fork of cmark) instead of building it from source
    "-DUSE_SYSTEM_LAYER_SHELL=ON",  # Use system qt layer shell instead of building it from source
    "-DUSE_SYSTEM_GLAZE=OFF",  # Use system glaze instead of fetching it. This is a header only library so only required at build time
    "-DUSE_SYSTEM_QT_KEYCHAIN=ON",  # Use system qt-keychain instead of building it from source. Note: still depends on system libsecret.
    "-DLIBQALCULATE_BACKEND=ON",  # Compile in support for the Qalculate! calculator backend
    "-DENABLE_SANITIZERS=OFF",  # Enable ASan + UBSan for debug builds
    "-DENABLE_PREVIEW_FEATURES=OFF",  # Enable preview features that are not yet ready for global release
    "-DUSE_PRECOMPILED_HEADERS=OFF",  # Use precompiled headers to speed up compilation; disabled for now, as it seems to be incompatible with ccache, and as such slows us down more than anything
]
hostmakedepends = ["ccache", "cmake", "git", "mold", "ninja", "pkgconf"]
makedepends = [
    "abseil-cpp-devel",
    # "cmark-devel",
    "glib-devel-static",
    "icu-libs",
    "layer-shell-qt-devel",
    "libqalculate-devel",
    # "libstdc++-static",
    "minizip-devel",
    "openssl3-devel",
    "protobuf-devel",
    "qt6-qtbase-devel",
    "qt6-qtbase-private-devel",
    "qt6-qtsvg-devel",
    "qt6-qtwayland-devel",
    "qtkeychain-devel",
    # "rapidfuzz-cpp-devel",
    "wayland-devel",
    "zlib-ng-devel",
    "zlib-ng-devel-static",
]
pkgdesc = (
    "Application launcher compatible with Raycast extensions, written in C++"
)
license = "GPL-3.0-only"
url = "https://vicinae.com"
source = (
    f"https://github.com/vicinaehq/vicinae/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "5bd3e1fd0bd76952e3c95bdb4364ea0c19bb6fb6274f79cb4932fd75073ce5b4"
