%define	pdir	XML
%define	pnam	Writer-String
%include	/usr/lib/rpm/macros.perl
Summary:	XML::Writer::String - Capture output from XML::Writer
Summary(pl.UTF-8):	XML::Writer::String - przechwytywanie wyjścia z modułu XML::Writer
Name:		perl-XML-Writer-String
Version:	0.1
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/S/SO/SOLIVER/XML-Writer-String-%{version}.tar.gz
# Source0-md5:	528b3ac5ec9d161fd28ff2ddfe65d3b9
URL:		http://search.cpan.org/dist/XML-Writer-String/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements a bare-bones class specifically for the purpose
of capturing data from the XML::Writer module. XML::Writer expects an
IO::Handle object and writes XML data to the specified object (or
STDOUT) via it's print() method. This module simulates such an object
for the specific purpose of providing the required print() method.

%description -l pl.UTF-8
Ten moduł implementuje niewielką klasę specjalnie do przechwytywania
danych z modułu XML::Writer. XML::Writer oczekuje obiektu IO::Handle i
zapisuje dane XML do podanego obiektu (lub na STDOUT) poprzez jego
metodę print(). Ten moduł symuluje taki obiekt w celu dostarczenia
wymaganej metody print().

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a example/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/XML/Writer
%{perl_vendorlib}/XML/Writer/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
