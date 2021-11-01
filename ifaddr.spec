#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ifaddr
Version  : 0.1.7
Release  : 27
URL      : https://files.pythonhosted.org/packages/3d/fc/4ce147e3997cd0ea470ad27112087545cf83bf85015ddb3054673cb471bb/ifaddr-0.1.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/3d/fc/4ce147e3997cd0ea470ad27112087545cf83bf85015ddb3054673cb471bb/ifaddr-0.1.7.tar.gz
Summary  : Cross-platform network interface and IP address enumeration library
Group    : Development/Tools
License  : MIT
Requires: ifaddr-license = %{version}-%{release}
Requires: ifaddr-python = %{version}-%{release}
Requires: ifaddr-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
=====================================================================

%package license
Summary: license components for the ifaddr package.
Group: Default

%description license
license components for the ifaddr package.


%package python
Summary: python components for the ifaddr package.
Group: Default
Requires: ifaddr-python3 = %{version}-%{release}

%description python
python components for the ifaddr package.


%package python3
Summary: python3 components for the ifaddr package.
Group: Default
Requires: python3-core
Provides: pypi(ifaddr)

%description python3
python3 components for the ifaddr package.


%prep
%setup -q -n ifaddr-0.1.7
cd %{_builddir}/ifaddr-0.1.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635741185
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ifaddr
cp %{_builddir}/ifaddr-0.1.7/LICENSE.txt %{buildroot}/usr/share/package-licenses/ifaddr/dbd6aca799aa635e17e93c8807f54f6aeeddb025
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ifaddr/dbd6aca799aa635e17e93c8807f54f6aeeddb025

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
