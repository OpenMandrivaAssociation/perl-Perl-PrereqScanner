%define upstream_name    Perl-PrereqScanner
%define upstream_version 1.002

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    A tool to scan your Perl code for its prerequisites
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Perl/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Spec::Functions)
BuildRequires: perl(File::Temp)
BuildRequires: perl(FindBin)
BuildRequires: perl(List::Util)
BuildRequires: perl(Moose)
BuildRequires: perl(Moose::Role)
BuildRequires: perl(PPI)
BuildRequires: perl(PPI::Document)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(String::RewritePrefix)
BuildRequires: perl(Test::More)
BuildRequires: perl(Try::Tiny)
BuildRequires: perl(Version::Requirements)
BuildRequires: perl(namespace::autoclean)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
The scanner will extract loosely your distribution prerequisites from your
files.

The extraction may not be perfect but tries to do its best. It will
currently find the following prereqs:

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml LICENSE README META.json
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%perl_vendorlib/*
