#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Protocol versioning
Summary(pl.UTF-8):	Wersjonowanie protokołów
Name:		ocaml-protocol_version_header
Version:	0.14.0
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/protocol_version_header/tags
Source0:	https://github.com/janestreet/protocol_version_header/archive/v%{version}/protocol_version_header-%{version}.tar.gz
# Source0-md5:	f06d8842b947b9b1d6aef10bf4866398
URL:		https://github.com/janestreet/protocol_version_header
BuildRequires:	ocaml >= 1:4.04.2
BuildRequires:	ocaml-core_kernel-devel >= 0.14
BuildRequires:	ocaml-core_kernel-devel < 0.15
BuildRequires:	ocaml-dune >= 2.0.0
BuildRequires:	ocaml-ppx_jane-devel >= 0.14
BuildRequires:	ocaml-ppx_jane-devel < 0.15
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
This library offers a lightweight way for applications protocols to
version themselves. The more protocols that add themselves to
Known_protocol, the nicer error messages we will get when connecting
to a service while using the wrong protocol.

This package contains files needed to run bytecode executables using
protocol_version_header library.

%description -l pl.UTF-8
Ta biblioteka oferuje lekki sposób na wersjonowanie protokołów
aplikacyjnych. Im więcej protokołów doda się do Known_protocol, tym
przyjemniejsze komunikaty błędów dostaniemy przy łączeniu się z usługą
przy użyciu niewłaściwego protokołu.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki protocol_version_header.

%package devel
Summary:	Protocol versioning - development part
Summary(pl.UTF-8):	Wersjonowanie protokołów - część programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-core_kernel-devel >= 0.14
Requires:	ocaml-ppx_jane-devel >= 0.14

%description devel
This package contains files needed to develop OCaml programs using
protocol_version_header library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki protocol_version_header.

%prep
%setup -q -n protocol_version_header-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/protocol_version_header/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/protocol_version_header

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.md README.org
%dir %{_libdir}/ocaml/protocol_version_header
%{_libdir}/ocaml/protocol_version_header/META
%{_libdir}/ocaml/protocol_version_header/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/protocol_version_header/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/protocol_version_header/*.cmi
%{_libdir}/ocaml/protocol_version_header/*.cmt
%{_libdir}/ocaml/protocol_version_header/*.cmti
%{_libdir}/ocaml/protocol_version_header/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/protocol_version_header/protocol_version_header.a
%{_libdir}/ocaml/protocol_version_header/*.cmx
%{_libdir}/ocaml/protocol_version_header/*.cmxa
%endif
%{_libdir}/ocaml/protocol_version_header/dune-package
%{_libdir}/ocaml/protocol_version_header/opam
