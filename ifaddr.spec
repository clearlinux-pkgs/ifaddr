#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ifaddr
Version  : 0.1.6
Release  : 6
URL      : https://files.pythonhosted.org/packages/9f/54/d92bda685093ebc70e2057abfa83ef1b3fb0ae2b6357262a3e19dfe96bb8/ifaddr-0.1.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/9f/54/d92bda685093ebc70e2057abfa83ef1b3fb0ae2b6357262a3e19dfe96bb8/ifaddr-0.1.6.tar.gz
Summary  : Enumerates all IP addresses on all network adapters of the system.
Group    : Development/Tools
License  : MIT
Requires: ifaddr-python = %{version}-%{release}
Requires: ifaddr-python3 = %{version}-%{release}
Requires: ipaddress
BuildRequires : buildreq-distutils3
BuildRequires : ipaddress

%description
ifaddr - Enumerate IP addresses on the local network adapters
        =============================================================
        
        `ifaddr` is a small Python library that allows you to find all the
        IP addresses of the computer. It is tested on **Linux**, **OS X**, and
        **Windows**. Other BSD derivatives like **OpenBSD**, **FreeBSD**, and
        **NetBSD** should work too, but I haven't personally tested those.
        
        This library is open source and released under the MIT License.
        
        You can install it with `pip install ifaddr`. It doesn't need to
        compile anything, so there shouldn't be any surprises. Even on Windows.
        
        ----------------------
        Let's get going!
        ----------------------

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

%description python3
python3 components for the ifaddr package.


%prep
%setup -q -n ifaddr-0.1.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1544388293
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
