#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : boto3
Version  : 1.17.58
Release  : 599
URL      : https://github.com/boto/boto3/archive/1.17.58/boto3-1.17.58.tar.gz
Source0  : https://github.com/boto/boto3/archive/1.17.58/boto3-1.17.58.tar.gz
Summary  : AWS SDK for Python
Group    : Development/Tools
License  : Apache-2.0
Requires: boto3-license = %{version}-%{release}
Requires: boto3-python = %{version}-%{release}
Requires: boto3-python3 = %{version}-%{release}
Requires: botocore
Requires: jmespath
Requires: s3transfer
BuildRequires : botocore
BuildRequires : buildreq-distutils3
BuildRequires : jmespath
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : s3transfer
BuildRequires : tox
BuildRequires : virtualenv

%description
Boto3 is the Amazon Web Services (AWS) Software Development Kit (SDK) for
Python, which allows Python developers to write software that makes use of
services like Amazon S3 and Amazon EC2.

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
Provides: pypi(boto3)
Requires: pypi(botocore)
Requires: pypi(jmespath)
Requires: pypi(s3transfer)

%description python3
python3 components for the boto3 package.


%prep
%setup -q -n boto3-1.17.58
cd %{_builddir}/boto3-1.17.58

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1619532480
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/boto3
cp %{_builddir}/boto3-1.17.58/LICENSE %{buildroot}/usr/share/package-licenses/boto3/598f87f072f66e2269dd6919292b2934dbb20492
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/boto3/598f87f072f66e2269dd6919292b2934dbb20492

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
