#
# Conditional build:
%bcond_without	tests	# do perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Test
%define	pnam	SimpleUnit
Summary:	%{pdir}::%{pnam} perl module
Summary(pl):	Modu³ perla %{pdir}::%{pnam}
Name:		perl-%{pdir}-%{pnam}
Version:	1.21
Release:	2
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	14395b9700959aa6c53c9b9b8d7de613
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Data-Compare
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a simplified Perl unit-testing framework for creating unit tests
to be run either standalone or under Test::Harness.

%description -l pl
To jest uproszczony szkielet dla testów poszczególnych czê¶ci aplikacji,
przeznaczony do uruchamiania niezale¿nego lub pod kontrol± Test::Harness.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
## author prefers to fuck with us :-/
%{__perl} -MExtUtils::MakeMaker -we 'WriteMakefile(NAME=>"Test::SimpleUnit")' \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README
%{perl_vendorlib}/%{pdir}/%{pnam}.pm
%{_mandir}/man3/*
