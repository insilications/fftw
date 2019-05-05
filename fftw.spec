Name     : fftw
Version  : 3.3.8
Release  : 23
URL      : http://www.fftw.org/fftw-3.3.8.tar.gz
Source0  : http://www.fftw.org/fftw-3.3.8.tar.gz
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
%setup -c -n fftw-3.3.8
cp -a fftw-3.3.8 ../fftw-3.3.8-single
cp -a fftw-3.3.8 ../fftw-3.3.8-double
cp -a fftw-3.3.8 ../fftw-3.3.8-long-double
cp -a fftw-3.3.8 ../fftw-3.3.8-double-avx2
cp -a fftw-3.3.8 ../fftw-3.3.8-single-avx2
cp -a fftw-3.3.8 ../fftw-3.3.8-double-avx512
cp -a fftw-3.3.8 ../fftw-3.3.8-single-avx512

%build
export AR=gcc-ar
export RANLIB=gcc-ranlib
export CFLAGS="$CFLAGS -ffunction-sections -falign-functions=32 -O3 -flto -fno-semantic-interposition -ffast-math "
export CXXFLAGS="$CXXFLAGS -ffunction-sections -falign-functions=32 -O3 -flto -fno-semantic-interposition "

pushd ../fftw-3.3.8-single
%configure --disable-static --enable-shared --enable-threads --enable-float --enable-sse2
make V=1  %{?_smp_mflags}
popd

pushd ../fftw-3.3.8-double
%configure --disable-static --enable-shared --enable-threads --enable-sse2 
make V=1  %{?_smp_mflags}
popd


pushd ../fftw-3.3.8-long-double
%configure --disable-static --enable-shared --enable-threads --enable-long-double 
make V=1  %{?_smp_mflags}
popd

export CFLAGS="$CFLAGS  -march=haswell -mtune=haswell"
export CXXFLAGS="$CXXFLAGS  -march=haswell -mtune-haswell"
pushd ../fftw-3.3.8-single-avx2
%configure --disable-static --enable-shared --enable-threads --enable-float --enable-avx2 --enable-fma --libdir=/usr/lib64/haswell
make V=1  %{?_smp_mflags}
popd

pushd ../fftw-3.3.8-double-avx2
%configure --disable-static --enable-shared --enable-threads --enable-avx2 --enable-fma --libdir=/usr/lib64/haswell
make V=1  %{?_smp_mflags}
popd

export CFLAGS="$CFLAGS  -march=skylake-avx512"
export CXXFLAGS="$CXXFLAGS  -march=skylake-avx512"
pushd ../fftw-3.3.8-single-avx512
%configure --disable-static --enable-shared --enable-threads --enable-float --enable-avx2 --enable-avx512 --enable-fma --libdir=/usr/lib64/haswell/avx512_1/
make V=1  %{?_smp_mflags}
popd
pushd ../fftw-3.3.8-double-avx512
%configure --disable-static --enable-shared --enable-threads --enable-avx2 --enable-avx512 --enable-fma --libdir=/usr/lib64/haswell/avx512_1/
make V=1  %{?_smp_mflags}
popd

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd ../fftw-3.3.8-single
make VERBOSE=1 V=1 %{?_smp_mflags} check
popd
pushd ../fftw-3.3.8-double
make VERBOSE=1 V=1 %{?_smp_mflags} check
popd
pushd ../fftw-3.3.8-long-double
make VERBOSE=1 V=1 %{?_smp_mflags} check
popd

%install
rm -rf %{buildroot}
pushd ../fftw-3.3.8-double-avx2
%make_install
popd
pushd ../fftw-3.3.8-single-avx2
%make_install
popd
pushd ../fftw-3.3.8-double-avx512
%make_install
popd
pushd ../fftw-3.3.8-single-avx512
%make_install
popd
pushd ../fftw-3.3.8-long-double
%make_install
popd
pushd ../fftw-3.3.8-single
%make_install
popd
pushd ../fftw-3.3.8-double
%make_install
popd

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
/usr/lib64/cmake/fftw3/FFTW3Config.cmake
/usr/lib64/cmake/fftw3/FFTW3ConfigVersion.cmake
/usr/lib64/cmake/fftw3/FFTW3fConfig.cmake
/usr/lib64/cmake/fftw3/FFTW3fConfigVersion.cmake
/usr/lib64/cmake/fftw3/FFTW3lConfig.cmake
/usr/lib64/cmake/fftw3/FFTW3lConfigVersion.cmake
%exclude /usr/lib64/haswell/avx512_1/cmake/fftw3/FFTW3Config.cmake
%exclude /usr/lib64/haswell/avx512_1/cmake/fftw3/FFTW3ConfigVersion.cmake
%exclude /usr/lib64/haswell/avx512_1/cmake/fftw3/FFTW3fConfig.cmake
%exclude /usr/lib64/haswell/avx512_1/cmake/fftw3/FFTW3fConfigVersion.cmake
%exclude /usr/lib64/haswell/cmake/fftw3/FFTW3Config.cmake
%exclude /usr/lib64/haswell/cmake/fftw3/FFTW3ConfigVersion.cmake
%exclude /usr/lib64/haswell/cmake/fftw3/FFTW3fConfig.cmake
%exclude /usr/lib64/haswell/cmake/fftw3/FFTW3fConfigVersion.cmake

%exclude /usr/lib64/haswell/avx512_1/*.so
%exclude /usr/lib64/haswell/libfftw3.so
%exclude   /usr/lib64/haswell/libfftw3f.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
/usr/lib64/haswell/*.so.*
/usr/lib64/haswell/avx512_1/*.so.*
