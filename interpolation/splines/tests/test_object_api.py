from __future__ import division

from numpy import *
from interpolation.cartesian import mlinspace

d = 2               # number of dimension
Ng = 1000           # number of points on the grid
K = int(Ng**(1/d))  # nb of points in each dimension
N = 10000           # nb of points to evaluate
a = array([0.0]*d, dtype=float)
b = array([1.0]*d, dtype=float)
orders = array([K]*d, dtype=int)

grid = mlinspace(a,b,orders)

# single valued function to interpolate
f = lambda vec: sqrt(vec.sum(axis=1))
# df

# # vector valued function
# g


# single valued function to interpolate
vals = f(grid)

print(vals)
mvals = concatenate([vals[:,None],vals[:,None]],axis=1)

print(mvals.shape)
# cubic
# multilinear
# one point
# multiple points
# gradient



# one single point
point = array([0.5, 0.5])

# many points
points = row_stack([[0.5, 0.5]]*N)



def test_object_api(Obj):

    cs = Obj(a,b,orders,vals)
    ii = cs(point)
    iii = cs(points)
    print('ii')
    print(ii)
    print(ii.shape)
    assert(ii.ndim==0)
    assert(isscalar(ii))
    assert(iii.ndim==1)
    assert(tuple(iii.shape)==(N,))


def test_object_vector_api(Obj):

    cs = Obj(a,b,orders,mvals)

    ii = cs(point)
    iii = cs(points)

    n_splines = mvals.shape[1]
    assert(ii.ndim==1)
    assert(tuple(ii.shape)==(n_splines,))
    assert(iii.ndim==2)
    assert(tuple(iii.shape)==(N,n_splines))

def test_object_vector_diff_api(Obj):

    cs = Obj(a,b,orders,mvals)

    # ii = cs(point, diff=True)
    iii, d_iii = cs.interpolate(points, diff=True)

    n_splines = mvals.shape[1]
    assert(iii.ndim==2)
    assert(tuple(iii.shape)==(N,n_splines))
    assert(tuple(d_iii.shape)==(N,d,n_splines))

def test_objects():

    from interpolation.splines import CubicSpline
    # test_object_api(CubicSpline)
    from interpolation.splines import CubicSplines
    # test_object_vector_api(CubicSplines)
    test_object_vector_diff_api(CubicSplines)

    from interpolation.splines.multilinear import LinearSpline
    test_object_api(LinearSpline)
    from interpolation.splines.multilinear import LinearSplines
    test_object_vector_api(LinearSplines)


if __name__ == '__main__':

    test_objects()
