#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Inline
%define		pnam	Tcl
Summary:	Inline::Tcl Perl module
Summary(cs.UTF-8):	Modul Inline::Tcl pro Perl
Summary(da.UTF-8):	Perlmodul Inline::Tcl
Summary(de.UTF-8):	Inline::Tcl Perl Modul
Summary(es.UTF-8):	Módulo de Perl Inline::Tcl
Summary(fr.UTF-8):	Module Perl Inline::Tcl
Summary(it.UTF-8):	Modulo di Perl Inline::Tcl
Summary(ja.UTF-8):	Inline::Tcl Perl モジュール
Summary(ko.UTF-8):	Inline::Tcl 펄 모줄
Summary(nb.UTF-8):	Perlmodul Inline::Tcl
Summary(pl.UTF-8):	Moduł Perla Inline::Tcl
Summary(pt.UTF-8):	Módulo de Perl Inline::Tcl
Summary(pt_BR.UTF-8):	Módulo Perl Inline::Tcl
Summary(ru.UTF-8):	Модуль для Perl Inline::Tcl
Summary(sv.UTF-8):	Inline::Tcl Perlmodul
Summary(uk.UTF-8):	Модуль для Perl Inline::Tcl
Summary(zh_CN.UTF-8):	Inline::Tcl Perl 模块
Name:		perl-Inline-Tcl
Version:	0.09
Release:	5
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c3f0a7852196b68a89128e54ce381f07
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Inline >= 0.40
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	tcl-devel >= 8.3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::Tcl - Write Perl subroutines in Tcl.

%description -l pl.UTF-8
Moduł Inline::Tcl - pozwalający na pisanie procedur Perla w Tcl-u.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL </dev/null \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

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
