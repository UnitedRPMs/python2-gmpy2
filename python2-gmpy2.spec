%global srcname gmpy2

%global gitdate 20190220
%global commit0 c6eb9634ba5847f27eb996d9cbab64b0fe830a20
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

Name:           python2-%{srcname}
Version:        2.1.0
Release:        7%{?dist}
Summary:        Python interface to GMP, MPFR, and MPC

License:        LGPLv3+
URL:            https://pypi.python.org/pypi/gmpy2
Source0:        https://github.com/aleaxit/gmpy/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  libmpc-devel
BuildRequires:  mpfr-devel
BuildRequires:  python2
BuildRequires:  python2-devel
BuildRequires:  python2dist(cython)
BuildRequires:  python2dist(setuptools)
BuildRequires:  python2dist(sphinx)
Provides:	gmpy

%description
This package contains a C-coded Python extension module that supports 
multiple-precision arithmetic.  It is the successor to the original 
gmpy module.  The gmpy module only supported the GMP multiple-precision 
library.  Gmpy2 adds support for the MPFR (correctly rounded real 
floating-point arithmetic) and MPC (correctly rounded complex 
floating-point arithmetic) libraries.  It also updates the API and 
naming conventions to be more consistent and support the additional 
functionality.


%prep
%autosetup -n gmpy-%{commit0}

# Fix file encodings.  First the easy one.
iconv -f ISO8859-1 -t UTF-8 src/gmpy2.c > src/gmpy2.c.utf8
touch -r src/gmpy2.c src/gmpy2.c.utf8
mv -f src/gmpy2.c.utf8 src/gmpy2.c

# Now the hard one.  What weird encoding is this, anyway?
sed -i.orig 's/i\xad/\xc3\xad/' src/mpz_pylong.c
touch -r src/mpz_pylong.c.orig src/mpz_pylong.c
rm src/mpz_pylong.c.orig

# Update the sphinx theme name
sed -i "s/'default'/'classic'/" docs/conf.py

%build
%py2_build
make -C docs html

%install
%py2_install

%check
PYTHONPATH=%{buildroot}%{python2_sitearch} %{__python2} test/runtests.py

%files 
%license COPYING COPYING.LESSER
%doc docs/_build/html/*
%{python2_sitearch}/%{srcname}*

%changelog

* Mon Feb 18 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2.1.0-7
- Updated to 2.1.0-7
- Upstream

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-0.7.a4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 15 2018 Jerry James <loganjerry@gmail.com> - 2.1.0-0.6.a4
- Update to alpha 4
- Drop python2 subpackage (bz 1647371)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-0.5.a2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Jerry James <loganjerry@gmail.com> - 2.1.0-0.4.a2
- Take 2 on the -addzero patch

* Tue Jun 26 2018 Jerry James <loganjerry@gmail.com> - 2.1.0-0.3.a2
- Add -addzero patch to fix bogus results in sympy

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-0.2.a2
- Rebuilt for Python 3.7

* Sat Jun  2 2018 Jerry James <loganjerry@gmail.com> - 2.1.0-0.1.a2
- Update to alpha version for sagemath 8.2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.0.8-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jun 28 2016 Jerry James <loganjerry@gmail.com> - 2.0.8-1
- New upstream release
- Drop upstreamed -decref patch

* Fri Mar 25 2016 Jerry James <loganjerry@gmail.com> - 2.0.7-4
- Add -decref patch

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb  1 2016 Jerry James <loganjerry@gmail.com> - 2.0.7-2
- Comply with latest python packaging guidelines

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sat Aug 22 2015 Jerry James <loganjerry@gmail.com> - 2.0.7-1
- New upstream release

* Mon Jul  6 2015 Jerry James <loganjerry@gmail.com> - 2.0.6-1
- New upstream release

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 19 2015 Jerry James <loganjerry@gmail.com> - 2.0.5-1
- New upstream release
- Drop patch for 32-bit systems, fixed upstream

* Mon Oct 13 2014 Jerry James <loganjerry@gmail.com> - 2.0.4-1
- New upstream release

* Fri Sep 12 2014 Jerry James <loganjerry@gmail.com> - 2.0.3-2
- BR python2-devel instead of python-devel
- Provide bundled(jquery)

* Fri Sep  5 2014 Jerry James <loganjerry@gmail.com> - 2.0.3-1
- Initial RPM
