%define upstream_name    Test-WWW-Selenium-Catalyst
%define upstream_version 0.07

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1

Summary:	Test your Catalyst app with Selenium
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://git.shadowcat.co.uk/catagits/Test-WWW-Selenium-Catalyst
Source0:	https://cpan.metacpan.org/authors/id/B/BO/BOBTFISH/Test-WWW-Selenium-Catalyst-%{upstream_version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
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


%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.60.0-2mdv2011.0
+ Revision: 656973
- rebuild for updated spec-helper

* Sat Dec 25 2010 Shlomi Fish <shlomif@mandriva.org> 0.60.0-1mdv2011.0
+ Revision: 624902
- import perl-Test-WWW-Selenium-Catalyst

