Summary:	Python package for mapping URLs to dicts and vice versa
Summary(pl.UTF-8):	Pakiet Pythona do odwzorowywania URL-i na słowniki i odwrotnie
Name:		python-Routes
Version:	1.12.3
Release:	1
License:	BSD (?)
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/R/Routes/Routes-%{version}.tar.gz
# Source0-md5:	9740ff424ff6b841632c784a38fb2be3
URL:		http://routes.groovie.org/
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	python-setuptools >= 0.6-0.a11.1
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
Requires:	python-WebOb
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Routes is a Python re-implementation of the Rails routes system for
mapping URLs to Controllers/Actions and generating URLs. Routes
makes it easy to create pretty and concise URLs that are RESTful with
little effort.

%description -l pl.UTF-8
Routes to pythonowa reimplementacja systemu przekierowań Rails do
odwzorowywania URL-i na kontrolery/akcje i generowania URL-i. Routes
ułatwia tworzenie ładnych i zwięzłych URL-i, spokojnych przy
niewielkim wysiłku.

%prep
%setup -q -n Routes-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--single-version-externally-managed \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG docs/
%{py_sitescriptdir}/Routes*
%{py_sitescriptdir}/routes*
