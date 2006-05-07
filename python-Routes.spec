Summary:	Python package for  mapping URL's to dicts and vice versa
Name:		python-Routes
Version:	1.3.2
Release:	1
Group:		Development/Languages/Python
License:	BSD (?)
Source0:	http://cheeseshop.python.org/packages/source/R/Routes/Routes-%{version}.tar.gz
# Source0-md5:	967fe418f3afb8fb49d0be99d835b6bc
URL:		http://wsgiarea.pocoo.org/colubrid/
BuildRequires:	python-devel
BuildRequires:	python-setuptools >= 0.6-0.a11.1
%pyrequires_eq  python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Routes is a Python re-implementation of the Rails routes system for mapping
URL's to Controllers/Actions and generating URL's. Routes makes it easy to
create pretty and concise URL's that are RESTful with little effort.

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

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py -exec rm -f \{\} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG docs/
%{py_sitescriptdir}/Routes*
%{py_sitescriptdir}/routes*
