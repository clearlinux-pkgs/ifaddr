#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ifaddr
Version  : 0.1.4
Release  : 2
URL      : https://files.pythonhosted.org/packages/12/40/97ef30db32e0c798fc557af403ea263dbeae8d334571603f02e19f4021a0/ifaddr-0.1.4.zip
Source0  : https://files.pythonhosted.org/packages/12/40/97ef30db32e0c798fc557af403ea263dbeae8d334571603f02e19f4021a0/ifaddr-0.1.4.zip
Summary  : Enumerates all IP addresses on all network adapters of the system.
Group    : Development/Tools
License  : MIT
Requires: ifaddr-python3
Requires: ifaddr-python
Requires: ipaddress
BuildRequires : buildreq-distutils3
BuildRequires : ipaddress

%description
ifaddr - Enumerate IP addresses on the local network adapters
        =============================================================
        
        `ifaddr` is a small Python library that allows you to find all the
        IP addresses of the computer. It is tested on **Linux**, **OS X**, and
        **Windows**.
        
        This library is open source and released under the MIT License.
        
        You can install it with `pip install ifaddr`. It doesn't need to
        compile anything, so there shouldn't be any surprises. Even on Windows.
        
        ----------------------
        Let's get going!
        ----------------------

%package python
Summary: python components for the ifaddr package.
Group: Default
Requires: ifaddr-python3

%description python
python components for the ifaddr package.


%package python3
Summary: python3 components for the ifaddr package.
Group: Default
Requires: python3-core

%description python3
python3 components for the ifaddr package.


%prep
%setup -q -n ifaddr-0.1.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1537282912
python3 setup.py build

%install
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
