Summary:	The MM and QM calculations library
Summary(pl):	Biblioteka do obliczeñ z zakresu mechaniki molekularnej i kwantowej
Name:		libghemical
Version:	2.00
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://www.uku.fi/~thassine/projects/download/%{name}-%{version}.tar.gz
# Source0-md5:	19ee087b6f3c0ce816ed1722b4a5b002
URL:		http://www.uku.fi/~thassine/projects/libghemical/
BuildRequires:	libstdc++-devel
BuildRequires:	mopac7-devel >= 1.2.5
BuildRequires:	mpqc-devel >= 1.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The MM and QM calculations library.

%description -l pl
Biblioteka do obliczeñ z zakresu mechaniki molekularnej i kwantowej.

%package devel
Summary:	Header files for libghemical library
Summary(pl):	Pliki nag³ówkowe biblioteki libghemical
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
Requires:	mopac7-devel >= 1.2.5
Requires:	mpqc-devel >= 1.10

%description devel
Header files for libghemical library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libghemical.

%package static
Summary:	Static libghemical library
Summary(pl):	Statyczna biblioteka libghemical
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libghemical library.

%description static -l pl
Statyczna biblioteka libghemical.

%prep
%setup -q

%build
%configure \
	--enable-mopac7 \
	--enable-mpqc
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog TODO
%attr(755,root,root) %{_libdir}/libghemical.so.*.*.*
%{_datadir}/libghemical

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libghemical.so
%{_libdir}/libghemical.la
%{_includedir}/ghemical
%{_pkgconfigdir}/libghemical.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libghemical.a
