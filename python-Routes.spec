Summary:	Python package for mapping URLs to dicts and vice versa
Summary(pl):	Pakiet Pythona do odwzorowywania URL-i na s³owniki i odwrotnie
Name:		python-Routes
Version:	1.5.2
Release:	1
License:	BSD (?)
Group:		Development/Languages/Python
Source0:	http://cheeseshop.python.org/packages/source/R/Routes/Routes-%{version}.tar.gz
# Source0-md5:	57ba126f9d63f0999fff13ff8cb9d41a
URL:		http://wsgiarea.pocoo.org/colubrid/
BuildRequires:	python-devel
BuildRequires:	python-setuptools >= 0.6-0.a11.1
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq  python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Routes is a Python re-implementation of the Rails routes system for
mapping URLs to Controllers/Actions and generating URLs. Routes
makes it easy to create pretty and concise URLs that are RESTful with
little effort.

%description -l pl
Routes to pythonowa reimplementacja systemu przekierowañ Rails do
odwzorowywania URL-i na kontrolery/akcje i generowania URL-i. Routes
u³atwia tworzenie ³adnych i zwiêz³ych URL-i, spokojnych przy
niewielkim wysi³ku.

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
