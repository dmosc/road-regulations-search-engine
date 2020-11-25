import articleMutations from './article/mutations'
import articleQueries from './article/queries'

const resolvers = {
  Query: {
    ...articleQueries
  },
  Mutation: {
    ...articleMutations
  }
}

export default resolvers
