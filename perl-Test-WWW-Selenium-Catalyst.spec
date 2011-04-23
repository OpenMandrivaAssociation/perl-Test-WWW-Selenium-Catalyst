%define upstream_name    Test-WWW-Selenium-Catalyst
%define upstream_version 0.06

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Test your Catalyst app with Selenium
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Alien::SeleniumRC)
BuildRequires: perl(Catalyst::Runtime)
BuildRequires: perl(Catalyst::Utils)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(IPC::Cmd)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::WWW::Selenium)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
no description found

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


