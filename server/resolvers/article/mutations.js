import { AVERAGE_WORDS_PER_MINUTE } from '../../utils/constants'
import { likesApi } from '../../endpoints'

const articleMutations = {
  articleLike: async (_, { id }) => {
    const payload = await likesApi(id);
    const data = payload.data
    console.log(data)
    return data
  }
}

export default articleMutations
