%define upstream_name    Perl-PrereqScanner
%define upstream_version 1.015
Name:		perl-%{upstream_name}
Version:	%perl_convert_version 1.015
Release:	3

Summary:	A tool to scan your Perl code for its prerequisites
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Perl/Perl-PrereqScanner-1.015.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Moose::Role)
BuildRequires:	perl(PPI)
BuildRequires:	perl(PPI::Document)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(String::RewritePrefix)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Try::Tiny)
BuildRequires:	perl(Version::Requirements)
BuildRequires:	perl(namespace::autoclean)
BuildRequires:	perl(CPAN::Meta::Requirements)

BuildArch:	noarch

%description
The scanner will extract loosely your distribution prerequisites from your
files.

The extraction may not be perfect but tries to do its best. It will
currently find the following prereqs:

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
%doc Changes META.yml LICENSE README META.json
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Tue May 31 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.4.0-1mdv2011.0
+ Revision: 682141
- update to new version 1.004

* Sun May 22 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.0-1
+ Revision: 677377
- update to new version 1.003

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.2.0-2
+ Revision: 657822
- rebuild for updated spec-helper

* Thu Feb 03 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.0-1
+ Revision: 635543
- update to new version 1.002

* Fri Jan 07 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.0-1mdv2011.0
+ Revision: 629500
- update to new version 1.001

* Wed Dec 08 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.0-1mdv2011.0
+ Revision: 616216
- update to new version 1.000

* Mon Dec 06 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.101.892-1mdv2011.0
+ Revision: 612252
- update to new version 0.101892

* Fri Nov 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.101.891-1mdv2011.0
+ Revision: 596745
- adding missing buildrequires
- update to 0.101891

* Wed Jul 14 2010 Jérôme Quelin <jquelin@mandriva.org> 0.101.890-1mdv2011.0
+ Revision: 553020
- adding missing buildrequires:
- update to 0.101890

* Wed Apr 07 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.960-1mdv2010.1
+ Revision: 532715
- update to 0.100960

* Wed Mar 24 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.830-1mdv2010.1
+ Revision: 527220
- update to 0.100830

* Thu Mar 11 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.690-1mdv2010.1
+ Revision: 518083
- update to 0.100690

* Wed Mar 10 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.680-1mdv2010.1
+ Revision: 517304
- update to 0.100680

* Sun Mar 07 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.630-1mdv2010.1
+ Revision: 515366
- update to 0.100630

* Tue Feb 23 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.521-1mdv2010.1
+ Revision: 510102
- import perl-Perl-PrereqScanner


* Tue Feb 23 2010 cpan2dist 0.100521-1mdv
- initial mdv release, generated with cpan2dist

