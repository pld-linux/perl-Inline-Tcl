#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	Inline
%define		pname	Tcl
Summary:	Inline::Tcl Perl module
Summary(cs):	Modul Inline::Tcl pro Perl
Summary(da):	Perlmodul Inline::Tcl
Summary(de):	Inline::Tcl Perl Modul
Summary(es):	Módulo de Perl Inline::Tcl
Summary(fr):	Module Perl Inline::Tcl
Summary(it):	Modulo di Perl Inline::Tcl
Summary(ja):	Inline::Tcl Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Inline::Tcl ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Inline::Tcl
Summary(pl):	Modu³ Perla Inline::Tcl
Summary(pt):	Módulo de Perl Inline::Tcl
Summary(pt_BR):	Módulo Perl Inline::Tcl
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Inline::Tcl
Summary(sv):	Inline::Tcl Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Inline::Tcl
Summary(zh_CN):	Inline::Tcl Perl Ä£¿é
Name:		perl-Inline-Tcl
Version:	0.09
Release:	3
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pname}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Inline >= 0.40
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	tcl-devel >= 8.3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::Tcl - Write Perl subroutines in Tcl.

%description -l pl
Modu³ Inline::Tcl - pozwalaj±cy na pisanie procedur Perla w Tcl-u.

%prep
%setup -q -n %{pdir}-%{pname}-%{version}

%build
%{__perl} Makefile.PL </dev/null \
	INSTALLDIRS=vendor 
%{__make} OPTIMIZE="%{rpmcflags}"
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Bugs Changes README
%{perl_vendorarch}/Inline/Tcl.pm
%dir %{perl_vendorarch}/auto/Inline/Tcl
%{perl_vendorarch}/auto/Inline/Tcl/Tcl.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Inline/Tcl/Tcl.so
%{_mandir}/man3/*
