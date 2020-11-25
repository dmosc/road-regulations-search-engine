import {gql} from '@apollo/client'

const GET_ARTICLES = gql`
    query articles($search: String!) {
        articles(search: $search) {
            id
            number
            content
            minutesToRead
            likes
        }
    }
`

export {GET_ARTICLES}
