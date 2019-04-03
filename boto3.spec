#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : boto3
Version  : 1.9.127
Release  : 163
URL      : https://github.com/boto/boto3/archive/1.9.127/boto3-1.9.127.tar.gz
Source0  : https://github.com/boto/boto3/archive/1.9.127/boto3-1.9.127.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: boto3-license = %{version}-%{release}
Requires: boto3-python = %{version}-%{release}
Requires: boto3-python3 = %{version}-%{release}
Requires: botocore
Requires: jmespath
Requires: s3transfer
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
===============================
Boto 3 - The AWS SDK for Python
===============================

%package license
Summary: license components for the boto3 package.
Group: Default

%description license
license components for the boto3 package.


%package python
Summary: python components for the boto3 package.
Group: Default
Requires: boto3-python3 = %{version}-%{release}

%description python
python components for the boto3 package.


%package python3
Summary: python3 components for the boto3 package.
Group: Default
Requires: python3-core

%description python3
python3 components for the boto3 package.


%prep
%setup -q -n boto3-1.9.127

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554305889
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/boto3
cp LICENSE %{buildroot}/usr/share/package-licenses/boto3/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/boto3/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
