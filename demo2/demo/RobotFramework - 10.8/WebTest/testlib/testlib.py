# -*- coding=utf-8 -*-
'''
@creatdate: 2016-12-19
@author: YuhuiXu
@description
'''

from Selenium2Library import Selenium2Library
class testlib(Selenium2Library):

    """Added By Yuhuixu"""
    def if_page_contain_elemet(self, locator, loglevel='INFO'):
        '''
        Verifies that current page contains `locator` element.
        :param locator:
        :param loglevel:
        :return False/True
        '''
        if not self._is_element_present(locator):
            self.log_source(loglevel)
#             raise AssertionError("Page should have contained element '%s' "
#                                  "but did not" % locator)
            return False
        self._info("Current page contains element '%s'." % locator)
        return True

#-----------------table element--------------------------------------------------
    def get_table_rows(self, table_locator, loglevel='INFO'):
        """Return the rows of the table.
        
        Header and footer rows are included in the count.
        """
        table = self._table_element_finder.find(self._current_browser(), table_locator)
        if table is not None:
            rows = table.find_elements_by_xpath("./thead/tr")
            rows.extend(table.find_elements_by_xpath("./tbody/tr"))
            rows.extend(table.find_elements_by_xpath("./tfoot/tr"))
            return len(rows)
        self.log_source(loglevel)
        raise AssertionError("Table %s could not be found." % table_locator)

    def get_table_cols_at_row(self, table_locator, row, loglevel='INFO'):
        """Return the columns of the table in one row.
            
        Row number start from 1. It will count the columns at one row, 
        the argument 'row' is the row number which you should give it.
        """
        row = int(row)
        row_index = row - 1
        table = self._table_element_finder.find(self._current_browser(), table_locator)
        if table is not None:
            rows = table.find_elements_by_xpath("./thead/tr")
            if row_index >= len(rows): rows.extend(table.find_elements_by_xpath("./tbody/tr"))
            if row_index >= len(rows): rows.extend(table.find_elements_by_xpath("./tfoot/tr"))
            if row_index < len(rows):
                columns = rows[row_index].find_elements_by_tag_name('th')
                columns.extend(rows[row_index].find_elements_by_tag_name('td'))
                return len(columns)
        raise AssertionError("Table %s in row #%s could not be found." % (table_locator, str(row)))

    def click_element_at_table_cell(self, table_locator, row, column, loglevel='INFO'):
        """Click a table cell.

        Row and column number start from 1. Header and footer rows are
        included in the count. This means that also cell content from
        header or footer rows can be obtained with this keyword. To
        understand how tables are identified, please take a look at
        the `introduction`.
        """
        row = int(row)
        row_index = row - 1
        column = int(column)
        column_index = column - 1
        table = self._table_element_finder.find(self._current_browser(), table_locator)
        if table is not None:
            rows = table.find_elements_by_xpath("./thead/tr")
            if row_index >= len(rows): rows.extend(table.find_elements_by_xpath("./tbody/tr"))
            if row_index >= len(rows): rows.extend(table.find_elements_by_xpath("./tfoot/tr"))
            if row_index < len(rows):
                columns = rows[row_index].find_elements_by_tag_name('th')
                if column_index >= len(columns): columns.extend(rows[row_index].find_elements_by_tag_name('td'))
                if column_index < len(columns):
                    return columns[column_index].click()
        self.log_source(loglevel)
        raise AssertionError("Cell in table %s in row #%s and column #%s could not be found."
            % (table_locator, str(row), str(column)))

    def click_link_at_table_cell(self, table_locator, row, column, loglevel='INFO'):
        """Click link within a table cell.

        Row and column number start from 1. Header and footer rows are
        included in the count. This means that also cell content from
        header or footer rows can be obtained with this keyword. To
        understand how tables are identified, please take a look at
        the `introduction`.
        """
        row = int(row)
        row_index = row - 1
        column = int(column)
        column_index = column - 1
        table = self._table_element_finder.find(self._current_browser(), table_locator)
        if table is not None:
            rows = table.find_elements_by_xpath("./thead/tr")
            if row_index >= len(rows): rows.extend(table.find_elements_by_xpath("./tbody/tr"))
            if row_index >= len(rows): rows.extend(table.find_elements_by_xpath("./tfoot/tr"))
            if row_index < len(rows):
                columns = rows[row_index].find_elements_by_tag_name('th')
                if column_index >= len(columns): columns.extend(rows[row_index].find_elements_by_tag_name('td'))
                if column_index < len(columns):
                    return columns[column_index].find_element_by_tag_name('a').click()
        self.log_source(loglevel)
        raise AssertionError("Cell in table %s in row #%s and column #%s could not be found."
            % (table_locator, str(row), str(column)))

    def click_subelement_at_table_cell(self, table_locator, row, column, sub_element_xpath, loglevel='INFO'):
        """Click a sub element indentified classpath in a table cell.

        Row and column number start from 1. Header and footer rows are
        included in the count. This means that also cell content from
        header or footer rows can be obtained with this keyword. To
        understand how tables are identified, please take a look at
        the `introduction`.
        """
        row = int(row)
        row_index = row - 1
        column = int(column)
        column_index = column - 1
        table = self._table_element_finder.find(self._current_browser(), table_locator)
        if table is not None:
            rows = table.find_elements_by_xpath("./thead/tr")
            if row_index >= len(rows): rows.extend(table.find_elements_by_xpath("./tbody/tr"))
            if row_index >= len(rows): rows.extend(table.find_elements_by_xpath("./tfoot/tr"))
            if row_index < len(rows):
                columns = rows[row_index].find_elements_by_tag_name('th')
                if column_index >= len(columns): columns.extend(rows[row_index].find_elements_by_tag_name('td'))
                if column_index < len(columns):
                    return columns[column_index].find_element_by_xpath(sub_element_xpath).click()
        self.log_source(loglevel)
        raise AssertionError("Cell in table %s in row #%s and column #%s could not be found."
            % (table_locator, str(row), str(column)))

    def get_index_in_table_column(self, table_locator, col, expected, loglevel='INFO'):
        """get content's index in a specific column contains `content`.

        Row and column number start from 1. Header and footer rows are
        included in the count. However, the header and footer content
        will not be matched against 'expected'.

        See `Page Should Contain Element` for explanation about `loglevel` argument.
        """
        has_head=0
        element = self._table_element_finder.find_by_header(self._current_browser(), table_locator, None)
        if element is not None:
            has_head = 1
        index = self._table_element_finder.find_in_col(self._current_browser(), table_locator, col, expected)
        if index <= 0:
            self.log_source(loglevel)
            raise AssertionError("Column #%s in table identified by '%s' "
                   "should have contained text '%s'."
                   % (col, table_locator, expected))
        return index+has_head

    def get_index_in_table_row(self, table_locator, row, expected, loglevel='INFO'):
        """Get content's index in a specific table row contains `content`.

        Row and column number start from 1. Header and footer rows are
        included in the count. This means that also cell content from
        header or footer rows can be obtained with this keyword. To
        understand how tables are identified, please take a look at
        the `introduction`.

        See `Page Should Contain Element` for explanation about `loglevel` argument.
        """
        row = int(row)
        row_index = row - 1
        table = self._table_element_finder.find(self._current_browser(), table_locator)
        if table is not None:
            rows = table.find_elements_by_xpath("./thead/tr")
            if row_index >= len(rows): rows.extend(table.find_elements_by_xpath("./tbody/tr"))
            if row_index >= len(rows): rows.extend(table.find_elements_by_xpath("./tfoot/tr"))
            if row_index < len(rows):
                columns = rows[row_index].find_elements_by_tag_name('th')
                columns.extend(rows[row_index].find_elements_by_tag_name('td'))
                column_index = 0
                for element in columns:
                    column_index = column_index + 1
                    element_text = element.text
                    if element_text and expected in element_text:
                        return column_index
        self.log_source(loglevel)
        raise AssertionError("%s could not be found in row #%s of table %s."
            % (expected, str(row), table_locator))

    """Added By Yuhuixu"""
    def decode(self,customstr,mode='utf-8'):
        '''
        turn to unicode
        :param customstr:
        :param mode:
        '''
        return customstr.decode(mode)

    """Added By Yuhuixu"""
    def encode(self,customstr,mode='utf-8'):
        '''
        turn to gb2312
        :param customstr:
        :param mode:
        '''
        return customstr.encode(mode)

    """Added By Yuhuixu"""
    def select_from_list_by_text(self, locator, *texts):
        """Selects `*texts` from list identified by `locator`
    
        Select list keywords work on both lists and combo boxes. Key attributes for
        select lists are `id` and `name`. See `introduction` for details about
        locating elements.
        """
        if not texts:
            raise ValueError("No texts given.")
        items_str = "text(s) '%s'" % ", ".join(texts)
        self._info("Selecting %s from list '%s'." % (items_str, locator))
        select = self._get_select_list(locator)
        for text in texts:
            select.select_by_visible_text(text)