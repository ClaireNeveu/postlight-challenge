const photoUrl = (id: string) => `https://postlight-photos.com/img/${id}`

export interface WithUrlParams<T> { match: { params: T } }

export {
    photoUrl
}