#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : boto3
Version  : 1.9.102
Release  : 136
URL      : https://github.com/boto/boto3/archive/1.9.102.tar.gz
Source0  : https://github.com/boto/boto3/archive/1.9.102.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: boto3-license = %{version}-%{release}
Requires: boto3-python = %{version}-%{release}
Requires: boto3-python3 = %{version}-%{release}
Requires: botocore
Requires: jmespath
Requires: s3transfer
BuildRequires : buildreq-distutils23
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

%package legacypython
Summary: legacypython components for the boto3 package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the boto3 package.


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
%setup -q -n boto3-1.9.102

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551138234
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1551138234
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/boto3
cp LICENSE %{buildroot}/usr/share/package-licenses/boto3/LICENSE
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/boto3/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
