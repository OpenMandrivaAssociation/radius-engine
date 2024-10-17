%define name radius-engine
%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Name:		%{name}
Version:	0.7
Release:	%mkrel 1
Summary:	A Lua based real-time 2D graphics game engine
Group:		System/Libraries
License:	MIT
URL:		https://radius-engine.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/%{name}/%{name}-%{version}.tar.gz
Patch0:		radius-engine-0.6-configure-lua.patch
Patch1:		radius-engine-0.7-shared.patch
BuildRequires:	lua-devel
BuildRequires:	SDL-devel
BuildRequires:	mesagl-devel
BuildRequires:	mesaglu-devel
BuildRequires:	physfs-devel
BuildRequires:	png-devel
BuildRequires:	zlib-devel
BuildRequires:	SDL_sound-devel

%description
Radius Engine is a Lua script-based real-time 2D graphics engine designed for 
rapidly prototyping games. Built on top of SDL and OpenGL, games made with 
Radius Engine are portable to both Windows and Linux.

%package -n %{libname}
Summary:	A Lua based real-time 2D graphics game engine
Group:		System/Libraries

%description -n %{libname}
Radius Engine is a Lua script-based real-time 2D graphics engine designed for 
rapidly prototyping games. Built on top of SDL and OpenGL, games made with 
Radius Engine are portable to both Windows and Linux.


%package -n %{develname}
Summary:	Development libraries and headers for Radius Engine
Group:		Development/C
Requires:	lua-devel
Requires:	SDL-devel
Requires:	mesagl-devel
Requires:	mesaglu-devel
Requires:	physfs-devel
Requires:	png-devel
Requires:	zlib-devel
Requires:	SDL_sound-devel
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Development libraries and headers for Radius Engine.

%prep
%setup -q
%patch0 -p1 -b .lua
%patch1 -p1 -b .shared
autoreconf -if
chmod -x *.c *.h ChangeLog

%build
%configure
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std

%__rm -f %{buildroot}%{_datadir}/doc/radius-engine/ChangeLog
%__rm -f %{buildroot}%{_libdir}/*.a

%clean
%__rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root,-)
%doc ChangeLog
%{_libdir}/libradius-engine.so.*

%files  -n %{develname}
%defattr(-,root,root,-)
%{_includedir}/radius.h
%{_libdir}/libradius-engine.so
%{_libdir}/libradius-engine.la
%{_libdir}/pkgconfig/radius-engine.pc

