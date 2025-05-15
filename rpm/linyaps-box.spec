%global debug_package %{nil}
Name:           linglong-box
Version:        1.4.3
Release:        1
Summary:        Linglong sandbox
License:        LGPLv3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}/linglong-box-%{version}.tar

BuildRequires:  cmake gcc-c++ glib2-devel glibc-static libstdc++-static gtest-devel gmock-devel libseccomp-devel libcap-devel

%description
Linglong sandbox with OCI standard.

%prep
%autosetup -p1 -n linglong-%{version}

%define _debugsource_template %{nil}

%build
mkdir build && cd build
cmake -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
      -DCMAKE_POSITION_INDEPENDENT_CODE=ON \
      -DBUILD_SHARED_LIBS=OFF \
      -Dlinyaps-box_CPM_LOCAL_PACKAGES_ONLY=ON ..
%make_build

%install
cd build
%make_install INSTALL_ROOT=%{buildroot}


%files
%doc README.md
%license LICENSE
%exclude %{_libdir}/cmake/linglong-*/*.cmake
%{_bindir}/ll-box

%changelog
* Wed May 14 2025 wurongjie <wurongjie@deepin.org> - 1.8.1-1
- Init project