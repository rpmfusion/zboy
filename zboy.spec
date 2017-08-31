Name:           zboy
Version:        0.60
Release:        5%{?dist}
Summary:        A GameBoy emulator

License:        GPLv3
URL:            http://zboy.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Fix format strings
# http://sourceforge.net/p/zboy/code/75/
Patch0:         %{name}-0.60-sfmt.patch
# Fix compiling with GCC 5.1
# http://sourceforge.net/p/zboy/code/85/
Patch1:         %{name}-0.60-mbc5.patch

BuildRequires:  SDL2-devel


%description
zBoy is a multiplatform GameBoy emulator that provides a load/save feature,
can perform PCX screenshots either manually or automatically (every few
seconds) and emulates an internal battery for ROMs that were designed to use
one (this allows to use the internal save option provided by such games,
remember highest scores, etc).
  
zBoy supports some additional features, too, like intelligent saving of
hi-scores for some games that aren't able to save their hi-scores table by
themselves because of the lack of a battery-backed RAM on the cartridge, and
improving screen's resolution output using graphic algorithms like Scale2x,
Scale3x, eagle... 

It is also one of the very few GameBoy emulators that provides a 2-gameboys 
link emulation, which makes it possible to play some games in 2-players mode 
on a LAN.


%prep
%setup -q
%patch0 -p0
%patch1 -p0

# Use standard Fedora CFLAGS to compile
sed -i 's/^CFLAGS = -s -std=gnu89 -O3 -Wall -Wextra -pedantic -Werror=format-security -Wfatal-errors -Wstrict-prototypes/CFLAGS += -std=gnu89/' Makefile.linux

# Fix end-of-line encoding
for txtfile in license.txt history.txt todo.txt zboy.txt
do
    sed -i 's/\r//' $txtfile
done


%build
export CFLAGS="%{optflags}"
%make_build -f Makefile.linux


%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 %{name} %{buildroot}%{_bindir}


%files
%{_bindir}/%{name}
%license license.txt
%doc colorize.txt history.txt todo.txt zboy.txt


%changelog
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

