#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Inline
%define		pnam	Tcl
Summary:	Inline::Tcl - Write Perl subroutines in Tcl
Summary(pl.UTF-8):	Inline::Tcl - pisanie procedur Perla w Tcl-u
Name:		perl-Inline-Tcl
Version:	0.09
Release:	5
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Inline/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c3f0a7852196b68a89128e54ce381f07
URL:		http://search.cpan.org/dist/Inline-Tcl/
BuildRequires:	perl-Inline >= 0.40
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	tcl-devel >= 8.3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Inline::Tcl Perl module allows you to put Tcl source code directly
"inline" in a Perl script or module. A Tcl interpreter is loaded and
the Tcl code is interpreted, then Perl asks the Tcl interpreter which
global procedures have been defined. Those functions are made
available to your Perl program as if they had been written in Perl.

%description -l pl.UTF-8
Moduł Perla Inline::Tcl pozwala na umieszczanie kodu źródłowego w
Tcl-u bezpośrednio w skryptach lub modułach perlowych. Wczytywany jest
interpreter Tcl-a, który interpretuje kod, a następnie Perl odpytuje
go, jakie procedury globalne zostały zdefiniowane. Funkcje te są
udostępniane programowi w Perlu tak, jakby były napisane w Perlu.

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
%attr(755,root,root) %{perl_vendorarch}/auto/Inline/Tcl/Tcl.so
%{_mandir}/man3/*
