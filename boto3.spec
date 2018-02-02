#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : boto3
Version  : 1.5.0
Release  : 16
URL      : https://pypi.debian.net/boto3/boto3-1.5.0.tar.gz
Source0  : https://pypi.debian.net/boto3/boto3-1.5.0.tar.gz
Summary  : The AWS SDK for Python
Group    : Development/Tools
License  : Apache-2.0
Requires: boto3-legacypython
Requires: boto3-python3
Requires: boto3-python
Requires: botocore
Requires: jmespath
Requires: s3transfer
BuildRequires : botocore
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : s3transfer
BuildRequires : setuptools

%description
Boto 3 - The AWS SDK for Python
        ===============================
        
        |Build Status| |Docs| |Version| |Gitter|
        
        Boto3 is the Amazon Web Services (AWS) Software Development Kit (SDK) for
        Python, which allows Python developers to write software that makes use
        of services like Amazon S3 and Amazon EC2. You can find the latest, most
        up to date, documentation at `Read the Docs`_, including a list of
        services that are supported. To see only those features which have been
        released, check out the `stable docs`_.

%package legacypython
Summary: legacypython components for the boto3 package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the boto3 package.


%package python
Summary: python components for the boto3 package.
Group: Default
Requires: boto3-legacypython
Requires: boto3-python3

%description python
python components for the boto3 package.


%package python3
Summary: python3 components for the boto3 package.
Group: Default
Requires: python3-core

%description python3
python3 components for the boto3 package.


%prep
%setup -q -n boto3-1.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1513704925
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1513704925
rm -rf %{buildroot}
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

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
