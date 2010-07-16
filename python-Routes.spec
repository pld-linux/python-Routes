Summary:	Python package for mapping URLs to dicts and vice versa
Summary(pl.UTF-8):	Pakiet Pythona do odwzorowywania URL-i na słowniki i odwrotnie
Name:		python-Routes
Version:	1.10.3
Release:	1
License:	BSD (?)
Group:		Development/Languages/Python
Source0:	http://cheeseshop.python.org/packages/source/R/Routes/Routes-%{version}.tar.gz
# Source0-md5:	03e2d9f2f6a1b7f9e4cfc3a3866e513f
URL:		http://routes.groovie.org/
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	python-setuptools >= 0.6-0.a11.1
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
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
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
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
