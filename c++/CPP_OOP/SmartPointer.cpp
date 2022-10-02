// Smart Pointer 구현
#pragma once

template <typename TYPE>
class eb_shared_ptr
{
public:
	eb_shared_ptr() ;
	explicit eb_shared_ptr(TYPE* ptr) ;
	eb_shared_ptr(const eb_shared_ptr<TYPE>& rhs) ;
	~eb_shared_ptr() ;

	void set(TYPE* ptr) noexcept;
	TYPE* get() const noexcept { return _ptr; };
	int   use_count() const noexcept { return (*_refCount); };
	bool  unique() const noexcept { return { _refCount ? (*_refCount == 0) : false}; }

	TYPE* operator->() { return _ptr; };
	TYPE& operator* () { return *_ptr; };
	operator bool() const { return (nullptr != _refCount); }
	eb_shared_ptr<TYPE>& operator=(const eb_shared_ptr<TYPE>& rhs);

private:
	void addRef() noexcept;
	void release() noexcept;

private:
	int* _refCount;
	TYPE* _ptr;
};