%include	/usr/lib/rpm/macros.perl
%define	pdir	Inline
%define	pname	Tcl
Summary:	Inline::Tcl perl module
Summary(pl):	Modu³ perla Inline::Tcl
Name:		perl-Inline-Tcl
Version:	0.09
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pname}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Inline >= 0.40
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	tcl-devel >= 8.3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::Tcl - Write Perl subroutines in Tcl.

%description -l pl
Modu³ Inline::Tcl - pozwalaj±cy na pisanie procedur Perla w Tcl-u.

%prep
%setup -q -n %{pdir}-%{pname}-%{version}

%build
perl Makefile.PL </dev/null
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Bugs Changes README
%{perl_sitearch}/Inline/Tcl.pm
%dir %{perl_sitearch}/auto/Inline/Tcl
%{perl_sitearch}/auto/Inline/Tcl/Tcl.bs
%attr(755,root,root) %{perl_sitearch}/auto/Inline/Tcl/Tcl.so
%{_mandir}/man3/*
