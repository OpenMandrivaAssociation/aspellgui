%define oname AspellGUI
%define debug_package	%{nil}
Name:		aspellgui
Summary:	GUI for aspell
License:	GPLv3
Version:	0.0.7
Release:	2
Group:		Text tools
URL:		http://keithhedger.hostingsiteforfree.com/pages/aspellgui/aspelgui.html
Source:		http://keithhedger.hostingsiteforfree.com/zips/aspellgui/%{oname}-%{version}.tar.gz
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  aspell-devel
BuildRequires:	desktop-file-utils
BuildRequires:	qmake5


%description
GUI for aspell, just launch it from the accessories menu and 
pase or type a word in the text box and either press 
\'Spell Check\' to check and correct all words in the 
text box or select a single word and press 
\'Check Word\' to just correct that one, 
that\'s all there is to it.


%prep
%setup -qn %{oname}-%{version}
perl -pi -e "s|gtk-update-icon-cache --ignore-theme-index --force /usr/share/icons/hicolor||"  AspellGUI/app/Makefile.in

%build
%configure --prefix=/usr --enable-qt5
make clean 
%make


%install
%makeinstall_std
desktop-file-validate %{buildroot}%{_datadir}/applications/AspellGUI.desktop 


%files
%doc  ChangeLog README AspellGUI/resources/docs/gpl-3.0.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{oname}.desktop
%{_datadir}/pixmaps/AspellGUI.png
%{_datadir}/pixmaps/AspellGUI48.png
%{_iconsdir}/hicolor/*/apps/AspellGUI.png
%{_datadir}/AspellGUI/
 
 
 
 
 
 
 
 
 
 
 
 