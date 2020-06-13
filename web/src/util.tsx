const photoUrl = (id: string) => `https://postlight-photos.com/img/${id}`

/**
 * For use with Props, e.g. type MyProps = { foo: int } & WithUrlParams<{ id: int }>
 */
export interface WithUrlParams<T> { match: { params: T } }

export interface WithQueryParams<T> { location: { query: T } }

export {
    photoUrl
}