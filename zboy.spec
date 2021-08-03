Name:           zboy
Version:        0.71
Release:        4%{?dist}
Summary:        A GameBoy Classic emulator

License:        GPLv3
URL:            http://zboy.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  SDL2-devel


%description
zBoy is a multi-platform, open-source GameBoy Classic ("DMG") emulator that
provides a load/save feature, can perform PCX screenshots and emulates an
internal battery for ROMs that were designed to use one. It is also one of
the very few emulators that make it possible to play games in 2-players mode
over LAN, emulating a link between two consoles.

zBoy supports many additional features, too, like intelligent saving of
hi-scores for some games that aren't able to save their hi-scores table by
themselves because of the lack of a battery-backed RAM on the cartridge, and
improving screen's resolution output using graphic algorithms like Scale2x,
Scale3x, Eagle...


%prep
%setup -q

# Use standard Fedora CFLAGS to compile
sed -i 's/^CFLAGS = -std=gnu89 -O3 -Wall -Wextra -pedantic -Werror=format-security -Wfatal-errors -Wstrict-prototypes/CFLAGS += -std=gnu89/' Makefile.linux
sed -i 's/^CFLAGS = -s -std=gnu89 -O3 -Wformat-security -Wall -Wextra -pedantic -Wno-long-long/CFLAGS += -std=gnu89/' libunzip/Makefile

# Fix LDLIBS
sed -i 's/LDFLAGS =/LDLIBS =/' Makefile.linux

# Fix end-of-line encoding
for txtfile in colorize.txt history.txt todo.txt zboy.txt
do
    sed -i 's/\r//' $txtfile
done


%build
%set_build_flags
%make_build -f Makefile.linux


%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 %{name} %{buildroot}%{_bindir}


%files
%{_bindir}/%{name}
%license license.txt
%doc colorize.txt history.txt todo.txt zboy.txt


%changelog
* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.71-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.71-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.71-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Feb 02 2020 Andrea Musuruane <musuruan@gmail.com> - 0.71-1
- Updated to new upstream release

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.70-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.70-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 26 2019 Andrea Musuruane <musuruan@gmail.com> - 0.70-1
- Updated to new upstream release

* Sun Aug 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.60-8
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.60-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.60-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.60-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 25 2017 Andrea Musuruane <musuruan@gmail.com> 0.60-4
- Fix FTBFS

* Tue Mar 21 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.60-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Oct 04 2015 Andrea Musuruane <musuruan@gmail.com> 0.60-2
- Correctly marked license file

* Thu May 14 2015 Andrea Musuruane <musuruan@gmail.com> 0.60-1
- First release

