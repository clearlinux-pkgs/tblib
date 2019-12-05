#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tblib
Version  : 1.5.0
Release  : 7
URL      : https://files.pythonhosted.org/packages/48/df/6a651c72d84ff136da474b4734212b8bc784bea771aa23cf32f2351e0cb7/tblib-1.5.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/48/df/6a651c72d84ff136da474b4734212b8bc784bea771aa23cf32f2351e0cb7/tblib-1.5.0.tar.gz
Summary  : Traceback serialization library.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: tblib-license = %{version}-%{release}
Requires: tblib-python = %{version}-%{release}
Requires: tblib-python3 = %{version}-%{release}
Requires: pip
Requires: setuptools
Requires: virtualenv
BuildRequires : buildreq-distutils3
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : util-linux
BuildRequires : virtualenv

%description
========
Overview
========
.. start-badges
.. list-table::
:stub-columns: 1
* - docs
- |docs|
* - tests
- | |travis| |appveyor| |requires|
| |codecov|
* - package
- | |version| |wheel| |supported-versions| |supported-implementations|
| |commits-since|
.. |docs| image:: https://readthedocs.org/projects/python-tblib/badge/?style=flat
:target: https://readthedocs.org/projects/python-tblib
:alt: Documentation Status

%package license
Summary: license components for the tblib package.
Group: Default

%description license
license components for the tblib package.


%package python
Summary: python components for the tblib package.
Group: Default
Requires: tblib-python3 = %{version}-%{release}

%description python
python components for the tblib package.


%package python3
Summary: python3 components for the tblib package.
Group: Default
Requires: python3-core

%description python3
python3 components for the tblib package.


%prep
%setup -q -n tblib-1.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571846021
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/tblib
cp %{_builddir}/tblib-1.5.0/LICENSE %{buildroot}/usr/share/package-licenses/tblib/77a5041738487df2388bbad74d9624f613500069
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tblib/77a5041738487df2388bbad74d9624f613500069

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
