%define upstream_name    Test-WWW-Selenium-Catalyst
%define upstream_version 0.07

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Test your Catalyst app with Selenium

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires: perl(Catalyst::EngineLoader)
BuildRequires:	perl(Alien::SeleniumRC)
BuildRequires:	perl(Catalyst::Runtime)
BuildRequires:	perl(Catalyst::Utils)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(IPC::Cmd)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::WWW::Selenium)
BuildArch:	noarch

%description
no description found

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*



