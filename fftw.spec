Name     : fftw
Version  : 3.3.4
Release  : 8
URL      : http://www.fftw.org/fftw-3.3.4.tar.gz
Source0  : http://www.fftw.org/fftw-3.3.4.tar.gz
Summary  : fast Fourier transform library
Group    : Development/Tools
License  : GPL-2.0
Requires: fftw-bin
Requires: fftw-lib
Requires: fftw-doc
BuildRequires: texinfo

%description
FFTW is a free collection of fast C routines for computing the
Discrete Fourier Transform in one or more dimensions.  It includes
complex, real, symmetric, and parallel transforms, and can handle
arbitrary array sizes efficiently.  FFTW is typically faster than
other publically-available FFT implementations, and is even
competitive with vendor-tuned libraries.  (See our web page
http://fftw.org/ for extensive benchmarks.)  To achieve this
performance, FFTW uses novel code-generation and runtime
self-optimization techniques (along with many other tricks).

%package bin
Summary: bin components for the fftw package.
Group: Binaries

%description bin
bin components for the fftw package.


%package dev
Summary: dev components for the fftw package.
Group: Development
Requires: fftw-lib
Requires: fftw-bin
Provides: fftw-devel

%description dev
dev components for the fftw package.


%package doc
Summary: doc components for the fftw package.
Group: Documentation

%description doc
doc components for the fftw package.


%package lib
Summary: lib components for the fftw package.
Group: Libraries

%description lib
lib components for the fftw package.


%prep
%setup -c -n fftw-3.3.4
ls
ls ..
mv fftw-3.3.4 fftw-3.3.4-single
cp -r fftw-3.3.4-single fftw-3.3.4-double
cp -r fftw-3.3.4-single fftw-3.3.4-long-double

%build
export AR=gcc-ar
export RANLIB=gcc-ranlib
export CFLAGS="$CFLAGS -ffunction-sections -falign-functions=32 -O3 -flto -fno-semantic-interposition -ffast-math "
export CXXFLAGS="$CXXFLAGS -ffunction-sections -falign-functions=32 -O3 -flto -fno-semantic-interposition "

cd fftw-3.3.4-single
%configure --disable-static --enable-shared --enable-threads --enable-float --enable-sse --enable-avx
make V=1  %{?_smp_mflags}
cd ../fftw-3.3.4-double
%configure --disable-static --enable-shared --enable-threads --enable-sse2 --enable-avx
make V=1  %{?_smp_mflags}
cd ../fftw-3.3.4-long-double
%configure --disable-static --enable-shared --enable-threads --enable-long-double
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
cd fftw-3.3.4-single
make VERBOSE=1 V=1 %{?_smp_mflags} check
cd ../fftw-3.3.4-double
make VERBOSE=1 V=1 %{?_smp_mflags} check
cd ../fftw-3.3.4-long-double
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
cd fftw-3.3.4-single
%make_install
cd ../fftw-3.3.4-double
%make_install
cd ../fftw-3.3.4-long-double
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/fftw-wisdom
/usr/bin/fftwf-wisdom
/usr/bin/fftwl-wisdom
/usr/bin/fftw-wisdom-to-conf

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/include/fftw3.f
/usr/include/fftw3.f03
/usr/include/fftw3l.f03
/usr/include/fftw3q.f03
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
