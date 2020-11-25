import {gql} from '@apollo/client'

const LIKE_ARTICLE = gql`
    mutation articleLike($id: ID!) {
        articleLike(id: $id) {
            likes
            id
        }
    }
`
export {LIKE_ARTICLE}