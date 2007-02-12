#
# Conditional build:
%bcond_without	tests	# do perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Test
%define		pnam	SimpleUnit
Summary:	Test::SimpleUnit - simplified Perl unit-testing framework
Summary(pl.UTF-8):   Test::SimpleUnit - uproszczony szkielet dla perlowych testów części aplikacji
Name:		perl-Test-SimpleUnit
Version:	1.21
Release:	3
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

%description -l pl.UTF-8
To jest uproszczony szkielet dla testów poszczególnych części aplikacji,
przeznaczony do uruchamiania niezależnego lub pod kontrolą Test::Harness.

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
%{perl_vendorlib}/Test/*.pm
%{_mandir}/man3/*
