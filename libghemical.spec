Summary:	The MM and QM calculations library
Summary(pl.UTF-8):	Biblioteka do obliczeń z zakresu mechaniki molekularnej i kwantowej
Name:		libghemical
Version:	2.99.1
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://bioinformatics.org/ghemical/download/current/%{name}-%{version}.tar.gz
# Source0-md5:	d2dae2d7d786d3cba335cb29d85033ea
URL:		http://bioinformatics.org/ghemical/ghemical/index.html
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel
BuildRequires:	intltool >= 0.40.0
BuildRequires:	lapack-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	mopac7-devel >= 1.13
BuildRequires:	mpqc-devel >= 1.2.5
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The MM and QM calculations library.

%description -l pl.UTF-8
Biblioteka do obliczeń z zakresu mechaniki molekularnej i kwantowej.

%package devel
Summary:	Header files for libghemical library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libghemical
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
Requires:	mopac7-devel >= 1.13
Requires:	mpqc-devel >= 1.2.5

%description devel
Header files for libghemical library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libghemical.

%package static
Summary:	Static libghemical library
Summary(pl.UTF-8):	Statyczna biblioteka libghemical
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libghemical library.

%description static -l pl.UTF-8
Statyczna biblioteka libghemical.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure \
	--enable-mopac7 \
	--enable-mpqc
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog TODO
%attr(755,root,root) %{_libdir}/libghemical.so.*.*.*
%{_datadir}/libghemical
%attr(755,root,root) %ghost %{_libdir}/libghemical.so.5

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libghemical.so
%{_libdir}/libghemical.la
%{_includedir}/ghemical
%{_pkgconfigdir}/libghemical.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libghemical.a
