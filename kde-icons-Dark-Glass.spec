%define		_name Dark-Glass
Summary:	KDE icons - %{_name}
Summary(pl.UTF-8):	Motyw ikon do KDE - %{_name}
Name:		kde-icons-%{_name}
Version:	1.2
Release:	1
License:	GPL
Group:		Themes
Source0:	http://www.mentalrey.it/icon_set/%{_name}.zip
# Source0-md5:	8028c44878b7f90a51ef1e0ac16f600d
Patch0:		%{_name}-Dos2Unix.patch
URL:		http://www.kde-look.org/content/show.php/Dark-Glass+Icons+Project?content=67902
BuildRequires:	unzip
Requires:	kdelibs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{_name} is an icon theme.

%description -l pl
%{_name} to motyw ikon dla KDE.

%prep
%setup -q -n %{_name}
%patch0 -p0
chmod 755 buildset
./buildset kmenu

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}

bunzip2 -df %{_name}.tar.bz2
tar -xf %{_name}.tar -C $RPM_BUILD_ROOT%{_iconsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_iconsdir}/*
