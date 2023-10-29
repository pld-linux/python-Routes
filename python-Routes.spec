#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit and functional tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Python package for mapping URLs to dicts and vice versa
Summary(pl.UTF-8):	Pakiet Pythona do odwzorowywania URL-i na słowniki i odwrotnie
Name:		python-Routes
Version:	2.5.1
Release:	1
License:	MIT
Group:		Development/Languages/Python
#Source0Download: https://pypi.org/simple/routes/
Source0:	https://files.pythonhosted.org/packages/source/R/Routes/Routes-%{version}.tar.gz
# Source0-md5:	8f1fab1924e00d11b14719a469a3e0a2
URL:		https://pypi.org/project/Routes/
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-setuptools >= 1:0.6-0.a11.1
%if %{with tests}
BuildRequires:	python-WebOb
BuildRequires:	python-nose
BuildRequires:	python-repoze.lru >= 0.3
BuildRequires:	python-six
BuildRequires:	python-soupsieve < 2.0
BuildRequires:	python-webtest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.5
BuildRequires:	python3-setuptools >= 1:0.6-0.a11.1
%if %{with tests}
BuildRequires:	python3-WebOb
BuildRequires:	python3-nose
BuildRequires:	python3-repoze.lru >= 0.3
BuildRequires:	python3-six
BuildRequires:	python3-soupsieve < 2.0
BuildRequires:	python3-webtest
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python-repoze.lru >= 0.3
BuildRequires:	python-six
BuildRequires:	sphinx-pdg-2
%endif
Requires:	python-WebOb
Requires:	python-modules >= 1:2.7
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

%package -n python3-Routes
Summary:	Python package for mapping URLs to dicts and vice versa
Summary(pl.UTF-8):	Pakiet Pythona do odwzorowywania URL-i na słowniki i odwrotnie
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-Routes
Routes is a Python re-implementation of the Rails routes system for
mapping URLs to Controllers/Actions and generating URLs. Routes
makes it easy to create pretty and concise URLs that are RESTful with
little effort.

%description -n python3-Routes -l pl.UTF-8
Routes to pythonowa reimplementacja systemu przekierowań Rails do
odwzorowywania URL-i na kontrolery/akcje i generowania URL-i. Routes
ułatwia tworzenie ładnych i zwięzłych URL-i, spokojnych przy
niewielkim wysiłku.

%package apidocs
Summary:	API documentation for Python Routes module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona Routes
Group:		Documentation

%description apidocs
API documentation for Python Routes module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona Routes.

%prep
%setup -q -n Routes-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
PYTHONPATH=$(pwd) \
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-2
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/tests
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGELOG.rst LICENSE.txt README.rst
%{py_sitescriptdir}/routes
%{py_sitescriptdir}/Routes-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-Routes
%defattr(644,root,root,755)
%doc CHANGELOG.rst LICENSE.txt README.rst
%{py3_sitescriptdir}/routes
%{py3_sitescriptdir}/Routes-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,modules,*.html,*.js}
%endif
